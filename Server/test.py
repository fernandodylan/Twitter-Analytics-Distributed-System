use admin
db.createUser(
  {
    user: "admindylan",
    pwd: "Distributedsystems1!", // or cleartext password
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)