//Dados do Pokemon
const nomePokemon = document.querySelector(".pokemom-name");
const numeroPokemon = document.querySelector(".pokemom-number");
const imagemPokemon = document.querySelector(".pokemom-imagem");
//Inputs
const formulario = document.querySelector(".form");
const input = document.querySelector(".input-search");
//Botãos
const btnPrev = document.querySelector(".btn-prev");
const btnNext = document.querySelector(".btn-next");
//Outras
let searchPokemon = 1;
//Buscando o Pokemon da API
const fetchPokemon = async (pokemon) => {
    const APIResponse = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`)

    if(APIResponse.status == 200){
    const data = await APIResponse.json();
    return data
    }
}
//Renderizando o Pokemon na Pokedex
const renderPokemon = async (pokemon) => {

    nomePokemon.innerHTML = 'Carregando...'

    const data = await fetchPokemon(pokemon)

    if(data){
    imagemPokemon.style.display = 'block';
    nomePokemon.innerHTML = data.name;
    numeroPokemon.innerHTML = data.id;
    imagemPokemon.src = data['sprites']['versions']['generation-v']['black-white']['animated']['front_default'];
    searchPokemon = data.id;
    } else{
        imagemPokemon.style.display = 'none';
        numeroPokemon.innerHTML = '';
        nomePokemon.innerHTML = 'Not Found :C'
    }
}
//Add evento de submit no formulario
formulario.addEventListener('submit', (event) => {
    event.preventDefault();
    renderPokemon(input.value.toLowerCase())
    input.value = ''
});
//Add evento de click no botão
btnPrev.addEventListener('click', () => {
    if(searchPokemon > 1){
    searchPokemon -= 1;
    renderPokemon(searchPokemon)
    }
});
btnNext.addEventListener('click', () => {
    searchPokemon += 1;
    renderPokemon(searchPokemon)
});
renderPokemon(searchPokemon)