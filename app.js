const API_KEY = 'db2f323a1e364f40a204d490b7cc5cb2';
const SCHOOL_NAME = '대진전자통신고등학교';

const gradeSelect = document.getElementById('gradeSelect');
const classSelect = document.getElementById('classSelect');
const dateInput = document.getElementById('dateInput');
const statusMessage = document.getElementById('statusMessage');
const resultTitle = document.getElementById('resultTitle');
const resultMeta = document.getElementById('resultMeta');
const timetableList = document.getElementById('timetableList');
const form = document.getElementById('timetableForm');

const template = document.getElementById('timetableItemTemplate');

const state = {
    officeCode: null,
    schoolCode: null,
};

const zeroPad = (value) => value.toString().padStart(2, '0');

function populateSelects() {
    [1, 2, 3].forEach((grade) => {
        const option = document.createElement('option');
        option.value = grade;
        option.textContent = `${grade}학년`;
        gradeSelect.appendChild(option);
    });

    for (let cls = 1; cls <= 10; cls += 1) {
        const option = document.createElement('option');
        option.value = cls;
        option.textContent = `${cls}반`;
        classSelect.appendChild(option);
    }

    const today = new Date();
    dateInput.value = today.toISOString().split('T')[0];
}

function setStatus(message, type = 'info') {
    statusMessage.textContent = message;
    statusMessage.className = `status ${type}`;
}

async function fetchSchoolInfo() {
    setStatus('학교 정보를 불러오는 중입니다...', 'info');
    const params = new URLSearchParams({
        KEY: API_KEY,
        Type: 'json',
        SCHUL_NM: SCHOOL_NAME,
    });

    try {
        const response = await fetch(`https://open.neis.go.kr/hub/schoolInfo?${params}`);
        if (!response.ok) {
            throw new Error('학교 정보를 불러오지 못했습니다.');
        }

        const data = await response.json();
        const schoolInfo = data?.schoolInfo?.[1]?.row?.[0];
        if (!schoolInfo) {
            throw new Error('학교 정보를 찾을 수 없습니다.');
        }

        state.officeCode = schoolInfo.ATPT_OFCDC_SC_CODE;
        state.schoolCode = schoolInfo.SD_SCHUL_CODE;
        setStatus(`학교 코드 연동 완료: ${schoolInfo.ATPT_OFCDC_SC_NM}`, 'success');
    } catch (error) {
        console.error(error);
        setStatus('학교 정보를 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.', 'error');
    }
}

function deriveAcademicInfo(dateString) {
    const date = new Date(dateString);
    const month = date.getMonth() + 1;
    let schoolYear = date.getFullYear();
    if (month < 3) {
        schoolYear -= 1;
    }
    const semester = month >= 3 && month <= 8 ? '1' : '2';
    return { schoolYear, semester };
}

async function fetchTimetable(grade, classNum, dateString) {
    if (!state.officeCode || !state.schoolCode) {
        throw new Error('학교 코드가 설정되지 않았습니다.');
    }

    const { schoolYear, semester } = deriveAcademicInfo(dateString);
    const params = new URLSearchParams({
        KEY: API_KEY,
        Type: 'json',
        pIndex: 1,
        pSize: 100,
        ATPT_OFCDC_SC_CODE: state.officeCode,
        SD_SCHUL_CODE: state.schoolCode,
        AY: schoolYear,
        SEM: semester,
        ALL_TI_YMD: dateString.replaceAll('-', ''),
        GRADE: grade,
        CLASS_NM: classNum,
    });

    const response = await fetch(`https://open.neis.go.kr/hub/hisTimetable?${params}`);
    if (!response.ok) {
        throw new Error('시간표를 불러오지 못했습니다.');
    }
    const data = await response.json();
    return data?.hisTimetable?.[1]?.row ?? [];
}

function renderTimetable(rows) {
    timetableList.innerHTML = '';
    if (!rows.length) {
        const placeholder = document.createElement('li');
        placeholder.className = 'placeholder';
        placeholder.textContent = '선택한 날짜의 시간표가 없습니다.';
        timetableList.appendChild(placeholder);
        return;
    }

    const sorted = [...rows].sort((a, b) => Number(a.PERIO) - Number(b.PERIO));
    sorted.forEach((row) => {
        const clone = template.content.cloneNode(true);
        clone.querySelector('.period').textContent = `${zeroPad(row.PERIO)}교시`;
        clone.querySelector('.subject').textContent = row.ITRT_CNTNT || '수업 정보 없음';
        clone.querySelector('.teacher').textContent = row.TEACHER_NM ? `${row.TEACHER_NM} 선생님` : '';
        timetableList.appendChild(clone);
    });
}

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const grade = gradeSelect.value;
    const classNum = classSelect.value;
    const dateString = dateInput.value;

    if (!dateString) {
        setStatus('날짜를 선택해 주세요.', 'error');
        return;
    }

    setStatus('시간표를 불러오는 중입니다...', 'info');
    resultTitle.textContent = `${grade}학년 ${classNum}반 시간표`;
    resultMeta.textContent = dateString.replaceAll('-', '.');

    try {
        const rows = await fetchTimetable(grade, classNum, dateString);
        renderTimetable(rows);
        const resultText = rows.length ? `${rows.length}개 교시` : '데이터 없음';
        resultMeta.textContent = `${dateString.replaceAll('-', '.')} · ${resultText}`;
        setStatus('시간표 불러오기를 완료했습니다.', 'success');
    } catch (error) {
        console.error(error);
        setStatus(error.message, 'error');
        timetableList.innerHTML = '<li class="placeholder">데이터를 가져오는 중 오류가 발생했습니다.</li>';
    }
});

populateSelects();
fetchSchoolInfo();
