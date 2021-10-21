Project Description
===================

This project helps in finding effective solution for Interview scheduling and management.


Problem
**************

1. Add candidate
2. Add interviewer
3. Interviewer confused in picking the timeslot
4. Availability of the Interviewer
5. Availability of the candidate
6. Length of the Interview
7. Confirmation / Change suggestion / Cancellation


Solution
********

1. Add candidate
    Sign up in with email

2. Add interviewer
    - Add by superuser
    - generate random password
    - option to change password

3. Picking the time slots
    - Lets fix the length of interview as 1 hr
    - Candidate should pick the available time slots
    - Interviewer should be pick the available time slots
    - Update engaged timeslots of interviewer as unavailable time or busy time
    - Run a task when a timeslot of a user is updated to auto update the interview time
    - Run a task in every 30 minutes to auto update the time interview time

4. Confirm / Update
    - Updation of interview time is not possible after (Interview time - 1 hr)
    - Once an update is made, auto update task will be executed
    - Cancellation is possible
