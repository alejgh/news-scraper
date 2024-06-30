db.createUser(
        {
            user: "sampleUser",
            pwd: "notverysecure",
            roles: [
                {
                    role: "readWrite",
                    db: "records_db"
                }
            ]
        }
);
db.createCollection("entries");