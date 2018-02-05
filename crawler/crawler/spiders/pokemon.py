import scrapy
import json

class PokemonSpider(scrapy.Spider):
    name = 'pokemon'

    def start_requests(self):
        yield scrapy.Request(url = 'https://pokemondb.net/pokedex/national', callback = self.parse)

    def parse(self, response):
        arr = []
        for card in response.css('span.infocard-tall'):
            url_details = card
            name  = card.css('.ent-name::text').extract_first()
            id    = card.css('small::text').extract_first()
            url_details = 'https://pokemondb.net/' + card.css('a.ent-name::attr(href)').extract_first()
            types = card.css('small.aside a::text').extract()
            
            arr.append({
                'id' : id,
                'name' : name,
                'url_details': url_details,
                'types' : types
            })
        
        #self.log(arr[:1])
        with open('pokemons.json', 'w') as f:
            json.dump(arr, f)

        #name = response.css('span.infocard-tall .ent-name::text').extract()
        #name = response.css('span.infocard-tall .ent-name::text').extract_first()
        ##print(name)
        #self.log('Pokemon Name : %s' % name)
        #id = response.css('span.infocard-tall small::text').extract()
        #id = [x for x in id if x[:1] == '#']
        #id = response.css('span.infocard-tall small::text').extract_first()
        #self.log('Pokemon Id : %s' % id)
        #type = response.css('span.infocard-tall small.aside a::text').extract()
        #type = response.css('span.infocard-tall small.aside a::text').extract_first()
        #self.log('Pokemon Type : %s' % type)
