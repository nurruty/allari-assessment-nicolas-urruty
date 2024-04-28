# Allari Assessment

This projects fulfills the requirements of the assessment...

## Installation

```
pip install -r requirements.txt
```

## Execution

To run the task run:

```
python allari_task.py <person_id>
```

If no **person_id** is passed, the console will return the following error:

```
Missing person ID
```

## Testing

To tun the test run

```
pytest
```

## Project Structure

The structure of the project is the following

### classes

Contains the two classes of the project Person and Contact

### connected_persons

Contains the solutions for part 2 and 3.2

### notebooks

This folder has two notebooks which goal is to showcase steps into the final solution.

### scripts

Contains the solutions for part 1 and part 3.1

### test

Contains 3 test suites

### utils

Contain utility functions of the project.

### allari_task.py

This is the main file of the project. It fulfills the requirements of Part4z

## About the usage of AI

As explained in the task's requirements the usage of AI was allowed. In this case it was only used to create the loading scripts.

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

Create a function called "load_persons_from_json" which loads a json file from a "file_path", where the returned value of the function should be a dict of Person.

```
