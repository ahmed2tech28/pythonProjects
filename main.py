import os
import sys

basicServer = '''const express = require("express");
const app = express();

app.use(express.json())

const port = 4500;

app.get("/", (req, res) => {
  res.send("welcome");
});

app.listen(port, () => console.log(`listening at port ${port}`));

'''

# New Comment
def createFolderIfNotExist(name):
    if not(os.path.exists(name)):
        os.mkdir(name)

def getCurrentFileName():
    return sys.argv[0].split("/")[-1]

def getreadyForNode():
    fileOFNODe = open("server.js", "w")
    fileOFNODe.write(basicServer)
    os.system("npm init --y")
    os.system("npm i express mongoose nodemon")
    createFolderIfNotExist("src")
    createFolderIfNotExist("public")
    createFolderIfNotExist("src/config")
    createFolderIfNotExist("src/model")
    createFolderIfNotExist("src/routes")
    createFolderIfNotExist("src/middlewhere")

getreadyForNode()

# os.remove(getCurrentFileName())
