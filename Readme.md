# ABN LOOKUP SERVICE 
A simple utility written in **Python** to make ABN Lookup effortless.

### Background
This project is developed as an initiative to demonstrate the
quickest and latest way to making calls to ABN SOAP apis. The XML
response from these APIs is transformed into Python native 
dictionary and list. This project is supplied with a testclass
to run and demonstrate how testcases can be organized.

### Setup
To run this project install pipenv in your working environment.
Then run below command to install dependencies.
- pipenv sync

In order to start pipenv shell run 
- pipenv shell

### Prerequisite (Obtain GUID)
To run the project successfully you need to obtain GUID which should
be placed in the return statement of get_guid() method. This
GUID can be obtained using following link
https://abr.business.gov.au/Documentation/WebServiceRegistration

### Running testcases
To run test cases, open your terminal/cmd and navigate to 
working directory and then run following command:
- python test_abnlookup.py

### Error
If no ABN/ACN/business name found then an exception is returned
in a dictionary object.

### Useful links
- https://www.abr.business.gov.au/
- https://abr.business.gov.au/abrxmlsearch/abrxmlsearch.asmx
- https://abr.business.gov.au/Documentation/WebServiceRegistration
- https://winthropdc.files.wordpress.com/2013/07/usingabnlookupwebservices.pdf

