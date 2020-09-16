pytest -s -v -m "sanity" --html=./Reports/reports.html testCases/
rem pytest -s -v -m "regression" --html=./Reports/reports.html testCases/
rem pytest -s -v -m "sanity or regression" --html=./Reports/reports.html testCases/
rem pytest -s -v -m "sanity and regression" --html=./Reports/reports.html testCases/

