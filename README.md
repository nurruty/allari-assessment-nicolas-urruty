# Allari Assessment - Nicolas Urruty

This project fulfills the criteria of the four-part assessment. It involves processing lists of Persons and Contacts (where Contacts represent the phone numbers associated with each Person). Upon running the script with a person ID, it returns a list of connected persons based the following rules:

<ol>

<li>
Two Persons are connected if they worked
for the same company and their timelines at the company overlap by at least 90 days. (For this
exercise, it is fine to assume that a person only has one entry per company. In other words, you can
assume that persons do not return to work for previous employers)
</li>
</br>
<li>
Two Persons are connected when
either one has the other’s phone number in their list of contacts.
</li>

</ol>

_Note: The definitions of Person and Contact are given_

## Installation

Open a new terminal. To ensure a safe execution environment, create a new virtual environment.

_Note: This assumes python3.x is being used._

If virtualenv is not installed, run:

```
pip install virtualenv
```

Then execute:

```
virtualenv allari-task
```

```
source activate allari-task
```

Finally, install the project's dependencies:

```
pip install -r requirements.txt
```

## Execution

Prior to execution, ensure that the `persons.json` and `contacts.json` files are present in the same directory as `allari_task.py`. A sample version of both files is already included in the repository.

To run the task, execute:

```
python allari_task.py <person_id>
```

If no **person_id** is provided, the console will return the following error:

```
$ python allari_task.py

Missing person ID
```

If **person_id** is not part of the list of Persons in persons.json an exception will be raised:

```
$ python allari_task.py 7

Exception: Person with ID 7 not found
```

If execution is successful, the list of connected persons with the specified **person_id** will be printed. For example, this is the output for the sample files with `person_id=1`:

```
$ python allari_task.py 1

0: Jane Doe
3: Tim Cook
4: Alan Turing
```

If there are no Persons connected to the provided **person_id**, the following message will be printed:

```
$ python allari_task.py 5

No connected Persons to person ID: 5
```

## Testing

Another requirement of the assessment was to create unit and integration tests.

The list of unit and integration tests includes:

<ul>
<li> test_overlaps_days </li>
<li> test_have_worked_together </li>
<li> test_get_connected_persons_by_job_person_exists </li>
<li> test_get_connected_persons_by_job_person_does_not_exist</li>
<li> test_get_contacts_by_person </li>
<li> test_get_contacts_by_person_no_contacts </li>
<li> test_get_connected_persons_by_contact </li>
<li> test_get_connected_persons_by_contact_person_not_found </li>
<li>test_get_connected_persons</li>
<li>test_get_no_connected_persons</li>
</ul>

To execute all tests run:

```
pytest
```

## Project Structure

A well-organized structure is crucial for a quality solution. In this case, the project is divided into separate modules that work together to fulfill the requirements.

```
allari-task-nicolas-urruty/
  classes/
      __init__.py
      person.py
      person.py
  connected_persons/
      __init__.py
      connected_persons_by_contact.py
      connected_persons_by_job.py
      connected_persons.py
  scripts/
      __init__.py
      load_contacts.py
      load_persons.py
  test/
      __init__.py
      test_connected_persons_by_contact.py
      test_connected_persons_by_job.py
      test_connected_persons.py
      test_contacts.json
      test_persons.json
      test_utils
  utils/
      utils.py
  .gitignore
  allari_task.py
  contacts.json
  persons.json
  README.md
  requirements.txt

```

### classes

Contains the two project classes: Person and Contact.

### connected_persons

Contains the solutions for parts 2, 3.2 and 4

### scripts

Contains the solutions for part 1 and part 3.1

### test

Contains three test suites

### utils

Contain utility functions for the project.

### allari_task.py

This is the main file of the project. It fulfills the requirements of Part 4.

## About the usage of AI

As explained in the task's requirements, the usage of AI was allowed. In this case, it was only used to create the loading scripts.

An example of the the prompt used is:

```
Act as an python expert. Given the following classes:


class Experience:
  def __init__(self, company, title, start, end):
    self.company = company
    self.title = title
    self.start = start
    self.end = end

class Person:
  def __init__(self, id, first, last, phone, experience):
    self.id = id
    self.first = first
    self.last = last
    self.phone = phone
    self.experience = experience


and having the following constraints:

- “id” values are unique
- the “phone” field may be null
- when not null, “phone” is a normalized string containing country code and phone
  number, separated by a dash
- “start” and “end” in an “experience” are normalized strings containing dates (null values
  for “end” mean the present)
- “experience” items are unique by “company”, i.e. there will not be multiple entries for the
  same person/company

Create a function called "load_persons_from_json" which loads a json file from a "file_path".

The returned value of the function should be a dict of Person.

```
