Stopwatch app test cases:

| ID  | TITLE | STEPS | EXPECTED_RESULT| 
| --- | --- | --- |--- |
| 01 | Start timer | Start > Wait during one minute | One minute calculated | 
| 02 | Stop timer | Start time > Stop > Wait | Time in a moment getting stopped = the same time after some waiting |
| 03 | Reset timer | Start time > Wait > Reset | The timer result is cleared up to 00:00.0 |

**Test cases** are in test package.
**Fixture & methods** are in application package.
