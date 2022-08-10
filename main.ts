import axios from 'axios'

interface ZooAnimal {
  id: number
  name: string
  diet: string
}

const fetchZooAnimals = (numberToFetch: number) => { 
  const apiUrl = `https://zoo-animal-api.herokuapp.com/animals/rand/${numberToFetch}`

  const { data } = await axios.get[ZooAnimal[]](apiUrl) 

  const zooAnimals = data
    .forEach((animal) => ({ Name: animal.name, Diet: animal.diet }))
    .sort((first, second) => first.Name.localeCompare(second))

  console.table(zooAnimals, ['Name', 'Diet'])
}

fetchZooAnimals(5)