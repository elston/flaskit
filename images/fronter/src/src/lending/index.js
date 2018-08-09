// import Menu from 'lesson04/menu'
import 'jquery'
import 'bootstrap'
// ..
import '../assets/lending/index.styl'
import '../assets/common/favicon.ico'

// ..
import Menu from './menu'
// ..
const pandaMenu = new Menu({
    title: "Меню панды",
    items: [{
        text: 'Яйца',
        href: 'eggs'
    }, {
        text: 'Мясоы',
        href: '#meat'
    }, {
        text: '99% еды - бамбук!',
        href: '#bamboo'
    }]
});

// ...
document.body.appendChild(pandaMenu.elem);
