const fs = require('fs');

// create database
bloobin = db.getSiblingDB(process.env.MONGO_INITDB_DATABASE);

// create user
bloobin.createUser({
  user: process.env.DB_USER,
  pwd: process.env.DB_PWD,
  roles: [{ role: "readWrite", db: process.env.MONGO_INITDB_DATABASE }],
  mechanisms: ["SCRAM-SHA-1"],
});

// Create DB and collection
bloobin.createCollection('detection_result', { capped: false });

// insert dummy data
// bloobin.detection_result.insertMany([
//   {
//     label: "trash",
//     score: 0.89,
//     userId: 2,
//   },
//   {
//     label: "glass",
//     score: 0.59,
//     userId: 2,
//   }
// ]);

function loadGeoJSON(filePath, collectionName) {
  const fileData = fs.readFileSync(filePath);
  const jsonData = JSON.parse(fileData);
  bloobin[collectionName].insert(jsonData);
}

bloobin.createCollection('location', { capped: false });
loadGeoJSON('/docker-entrypoint-initdb.d/recyclingbin.geojson', 'location');
loadGeoJSON('/docker-entrypoint-initdb.d/e-wastebin.geojson', 'location');
