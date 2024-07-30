#!/usr/bin/node

const fs = require("node:fs");

fs.readFile(process.argv[2], "utf-8", (error, data) => {
	if (error) {
		console.log(error);
	} else {
		console.log(data);
	}
});
