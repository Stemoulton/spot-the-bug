import axios from 'axios'

interface ZooAnimal {
  id: number
  name: string
  diet: string
}

// BUG - Missing async keyword, required for using await below
//const fetchZooAnimals = async (numberToFetch: number) => {
const fetchZooAnimals = (numberToFetch: number) => { 
  const apiUrl = `https://zoo-animal-api.herokuapp.com/animals/rand/${numberToFetch}`

  // BUG - Using the wrong syntax for declaring the type
  //const { data } = await axios.get<ZooAnimal[]>(apiUrl) 
  const { data } = await axios.get[ZooAnimal[]](apiUrl) 

  const zooAnimals = data
    // BUG - using a .forEach() rather than a .map(), .forEach() doesn't return anything
    //.map((animal) => ({ Name: animal.name, Diet: animal.diet }))
    .forEach((animal) => ({ Name: animal.name, Diet: animal.diet }))
    .sort((first, second) => first.Name.localeCompare(second))

  console.table(zooAnimals, ['Name', 'Diet'])
}

fetchZooAnimals(5)
