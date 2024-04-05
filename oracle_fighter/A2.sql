SELECT
    CONCAT(CONCAT(Z.FIRST_NAME, ' '),Z.LAST_NAME) EMPLOYEE_NAME,
    Z.SALARY,
    C.CITY,
    B.DEPARTMENT_NAME
FROM EMPLOYEES Z
LEFT JOIN DEPARTMENTS B
    ON Z.DEPARTMENT_ID = B.DEPARTMENT_ID
LEFT JOIN LOCATIONS C
    ON B.LOCATION_ID = C.LOCATION_ID
WHERE C.CITY = 'Seattle' AND B.DEPARTMENT_NAME = 'Executive'
