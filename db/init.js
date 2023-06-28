// create database
bloobin = db.getSiblingDB("bloobin_db");

// create user
bloobin.createUser({
  user: "bloobin_user",
  pwd: "bloobin_pwd",
  roles: [{ role: "readWrite", db: "bloobin_db" }],
  mechanisms: ["SCRAM-SHA-1"],
});

// Create DB and collection
bloobin.createCollection("detection_result", { capped: false });

// insert dummy data
bloobin.detection_result.insert(
  {
    label: "trash",
    score: 0.89,
    userId: 2,
  },
  {
    label: "glass",
    score: 0.59,
    userId: 2,
  }
);
