from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

# Create a connection to data access server
connection = ConnectionFactory.get_connection(url='localhost:5678')

# Get a store and assign it as a DocumentStore object
store = connection.get_store('/demo_table')

document_list = [{'_id': 'user0000',
                  'age': 35,
                  'firstName': 'John',
                  'lastName': 'Doe',
                  'address': {
                      'street': '350 Hoger Way',
                      'city': 'San Jose',
                      'state': 'CA',
                      'zipCode': 95134
                  },
                  'phoneNumbers': [
                      {'areaCode': 555, 'number': 5555555},
                      {'areaCode': '555', 'number': '555-5556'}]
                  },
                 {'_id': 'user0001',
                  'age': 26,
                  'firstName': 'Jane',
                  'lastName': 'Dupont',
                  'address': {
                      'street': '320 Blossom Hill Road',
                      'city': 'San Jose',
                      'state': 'CA',
                      'zipCode': 95196
                  },
                  'phoneNumbers': [
                      {'areaCode': 555, 'number': 5553827},
                      {'areaCode': '555', 'number': '555-6289'}]
                  },
                 {'_id': 'user0002',
                  'age': 45,
                  'firstName': 'Simon',
                  'lastName': 'Davis',
                  'address': {
                      'street': '38 De Mattei Court',
                      'city': 'San Jose',
                      'state': 'CA',
                      'zipCode': 95142
                  },
                  'phoneNumbers': [
                      {'areaCode': 555, 'number': 5425639},
                      {'areaCode': '555', 'number': '542-5656'}]
                  }
                 ]

for doc_dict in document_list:
    # Create new document from json_document
    new_document = connection.new_document(dictionary=doc_dict)
    # Print the OJAI Document
    print(new_document.as_json_str())

    # Insert the OJAI Document into the DocumentStore
    store.insert_or_replace(new_document)

# close the OJAI connection
connection.close()
