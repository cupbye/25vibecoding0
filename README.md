# Timetable Lookup Page

This project provides a static front-end that calls the NEIS timetable API for 대진전자통신고등학교.

## Previewing the page locally

Because everything is static (HTML, CSS, JavaScript), you only need a simple web server:

1. Make sure you are in the project directory.
2. Start a lightweight server. Any option that can serve static files will work, for example:
   ```bash
   python -m http.server 8000
   ```
3. Open your browser to [http://localhost:8000](http://localhost:8000) and click `index.html`.

Alternatively, open `index.html` directly from the file system in a browser, but some browsers block `fetch` calls from `file://` pages, so using a local server is recommended.

## Files
- `index.html` – markup and form controls for selecting grade, class, and date.
- `styles.css` – gradient/glassmorphism styling and responsive layout rules.
- `app.js` – logic for populating selects, deriving NEIS query parameters, calling the API, and rendering results.
