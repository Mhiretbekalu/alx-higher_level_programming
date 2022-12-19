#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
	print() {
		let rectangle = '';
		for (let i = 0; i < this.height; i++){
			for (let j = 0; j < this.width; j++){
				rectangle = rectangle + 'X';
				}
			console.log(rectangle);
			rectangle = '';
			}
	}
	rotate() {
		const rot = this.width;
		this.width = this.height;
		this.height = rot;
	}
	double() {
		this.width *= 2;
		this.height *= 2;
	}
}

module.exports = Rectangle;
