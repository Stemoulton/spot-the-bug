
import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"time"
)

type zooFact struct {
	Name      	string    	`json:"name"`
	LatinName 	string    	`json:"latinName"`
	AnimalType	string    	`json:"animalType"`
	ActiveTime	string		`json:"activeTime"`
	LengthMin	float64		`json:"lengthMin"`
	LengthMax	float64		`json:"lengthMax"`
	WeightMin   int       	`json:"weightMin"`
	WeightMax   int       	`json:"weightMin"`
	LifeSpan   	int       	`json:"lifeSpan"`
	Habitat		string		`json:"habitat"`
	Diet		string		`json:"diet"`
	GeoRange	string		`json:"geoRange"`
	ImageLink	string		`json:"imageLink"`
	id			int			`json:"_ID"`
}

func main() {
	res, err := http.Get("https://zoo-animal-api.herokuapp.com/animals/rand/?5")
	if err != nil {
		log.Printf("error on http request: %s\n", err)
	}

	resBody, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Printf("could not read response body: %s\n", err)
	}

	var zooFacts zoo

	err = json.Unmarshal(resBody, &zooFacts)
	if err != nil {
		log.Printf("could convert json: %s\n", err)
	}

	for _, fact := range zooFacts {
		fmt.Println("Name:", fact.Name, " - Diet:",  fact.Diet)
	}
}