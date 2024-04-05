SELECT
    BB.JOB_TITLE,
    AVG(AA.SALARY) AS AVG_SALARY
FROM EMPLOYEES AA
LEFT JOIN JOBS BB
    ON AA.JOB_ID = BB.JOB_ID
WHERE LOWER(BB.JOB_TITLE) = 'accountant'
    GROUP BY BB.JOB_TITLE
