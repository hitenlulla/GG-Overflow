let pgNav = document.querySelectorAll(".page__navigation-link")

const pg1 = pgNav[0]
const pg2 = pgNav[1]
const pg3 = pgNav[2]

pg1.addEventListener("click", () => {
	game1 = document.querySelector(".games--1")
	game2 = document.querySelector(".games--2")
	game3 = document.querySelector(".games--3")
	game1.style.display = "grid"
	game2.style.display = "none"
	game3.style.display = "none"
	pg1.classList.add("page__navigation-link--active")
	pg2.classList.remove("page__navigation-link--active")
	pg3.classList.remove("page__navigation-link--active")
})

pg2.addEventListener("click", () => {
	game1 = document.querySelector(".games--1")
	game2 = document.querySelector(".games--2")
	game3 = document.querySelector(".games--3")
	game1.style.display = "none"
	game2.style.display = "grid"
	game3.style.display = "none"
	pg1.classList.remove("page__navigation-link--active")
	pg2.classList.add("page__navigation-link--active")
	pg3.classList.remove("page__navigation-link--active")
})

pg3.addEventListener("click", () => {
	game1 = document.querySelector(".games--1")
	game2 = document.querySelector(".games--2")
	game3 = document.querySelector(".games--3")
	game1.style.display = "none"
	game2.style.display = "none"
	game3.style.display = "grid"
	pg1.classList.remove("page__navigation-link--active")
	pg2.classList.remove("page__navigation-link--active")
	pg3.classList.add("page__navigation-link--active")
})

const addToCart = document.querySelectorAll(".btn--addToCart")
const backdrop = document.getElementById("backdrop")
const modal = document.getElementById("modal")
const toggleBackdrop = () => {
	backdrop.classList.toggle("visible")
}
const toggleModal = () => {
	modal.classList.toggle("visible")
}

for (const a of addToCart) {
	a.addEventListener("click", () => {
		toggleBackdrop()
		toggleModal()
	})
}

const backdropClickHandler = () => {
	toggleBackdrop()
	toggleModal()
}
backdrop.addEventListener("click", backdropClickHandler)

const passiveBtn = document.querySelector(".btn--passive")
passiveBtn.addEventListener("click", () => {
	toggleBackdrop()
	toggleModal()
})
