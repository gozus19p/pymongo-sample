from pymongo_sample import sample

if __name__ == "__main__":
    # Creating connection, returning collection
    connection = sample.connect()

    # Declaring first key and first article
    key = "https://google.com/my-article#123"
    article = {
        "_id": key,
        "createdBy": "m.gozzi@isagog.com"
    }

    # Preparing some basic insert operation
    sample.insert(
        document=article,
        connection=connection
    )
    article_found = sample.find(key=key, connection=connection)
    assert article_found["_id"] == key

    # Setting `name`
    article_found["name"] = "My article"

    # Doing upsert
    sample.upsert(connection=connection, document=article_found, key=key)

    # Declaring other key, for another use case
    other_key = "https://google.com/my-article#456"
    sample.upsert(key=other_key, connection=connection, document={
        "_id": other_key,
        "createdBy": "m.gozzi@isagog.com",
        "name": "Another fabulous article"
    })

    # Querying for the first article
    first_article = sample.find(key=key, connection=connection)

    # Asserting that the name is compliant with the expectations
    assert first_article is not None and first_article["name"] == "My article"
    print(first_article)

    # Querying for the second article
    second_article = sample.find(key=other_key, connection=connection)

    # Asserting that the name is compliant with the expectations
    assert second_article is not None and second_article["name"] == "Another fabulous article"
    print(second_article)
    pass
