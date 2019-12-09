// @ts-check

var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');
var ObjectID = require('mongodb').ObjectID;

var url = 'mongodb://127.0.0.1:27017/test';

MongoClient.connect(url, (err, db) => {
    console.log(db);

    assert.equal(null, err);

    const users = db.collection('users');
    console.log(users)

    db.close();
    return;
});