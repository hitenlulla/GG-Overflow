const dataNav = document.querySelectorAll(".about-sidebar-lower-item")
const about1 = document.querySelector(".about--1")
const about2 = document.querySelector(".about--2")
const about3 = document.querySelector(".about--3")

for (const d of dataNav) {
	if (d == dataNav[0] || d == dataNav[3] || d == dataNav[6]) {
		d.addEventListener("click", () => {
			about1.style.display = "flex"
			about2.style.display = "none"
			about3.style.display = "none"
		})
	} else if (d == dataNav[1] || d == dataNav[4] || d == dataNav[7]) {
		d.addEventListener("click", () => {
			about1.style.display = "none"
			about2.style.display = "flex"
			about3.style.display = "none"
		})
	} else if (d == dataNav[2] || d == dataNav[5] || d == dataNav[8]) {
		d.addEventListener("click", () => {
			about1.style.display = "none"
			about2.style.display = "none"
			about3.style.display = "flex"
		})
	}
}
