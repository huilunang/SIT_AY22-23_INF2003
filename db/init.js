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
