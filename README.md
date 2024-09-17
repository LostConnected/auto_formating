# Auto Formatting

Auto formatting the data to let the code read.

## Reading Code:

```sas
input @1 Company $20. @25 State $2. @;
if State = " " then input @30 Year;
else input @30 City Year;
input NumEmployees;
```
