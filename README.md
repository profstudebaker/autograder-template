# Gradescope Autograder

This is an initial proof of concept of using the Gradescope Autograder to automatically check student submissions for required files and compilation errors, so students can see that their code failed and they received a 50% deduction before the deadline for the assignment ends. This immediate feedback will hopefully lead to more learning opportunities and fewer angry emails after grades are posted.

## How the Autograder Works

The autograder runs in a containerized environment inside Gradescope's Docker container after students have submitted their work.

`setup.sh` is run by the container to install all dependencies (like python3, jdk, etc) before evaluating the code

`run_autograder` is a bash script run after setup that can be used to copy in files over to the container from the student

`run_tests.py` is the main python script that will execute each test in the `/tests` directory and then compile the final score in the expected json output for Gradescope

Each test you want to execute should exist in its own file in the `/tests` directory. This example uses the python [unittest library](https://docs.python.org/3/library/unittest.html) to run tests and the [gradescope-utils library](https://github.com/gradescope/gradescope-utils) to assign weights, print messages to students, etc. This allows us to [write tests in python to evaluate output for any language](https://gradescope-autograders.readthedocs.io/en/latest/diff/), but you can also [write tests in a different language](https://gradescope-autograders.readthedocs.io/en/latest/java/).

## Creating a New Autograder

You should create a new autograder for each assignment. I am working on a generalized template, but it is not ready, so in the meantime just

1. Copy the contents of MP1 to a new subdirectory
2. Command+F for all occurences of "CHANGE" - I have left comments on all the lines sensitiviely referencing filenames that would break the grader in a different context. Change these lines to reflect your expected filenames for the new assignment.
3. Add or modify any tests.
4. Zip the entire directory (/tests and all the set up files in the root) and upload the .zip file to Gradescope
5. Test your autograder with both incorrect and correct solutions to evaluate its performance. Unfortunately testing local is a pain and I have not figured out a good system yet.

## Resources

- [Gradescope Autograder Documentation](https://gradescope-autograders.readthedocs.io/en/latest/)
