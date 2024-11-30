PREFIX odrl: <http://www.w3.org/ns/odrl/2/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX tosl: <http://www.w3.org/tosl/>

# action = to rerminate or suspend
SELECT ?permission ?action ?target ?constraint
WHERE {
    ?permission a odrl:Permission ;
        odrl:action ?action ;
        odrl:target ?target .
    FILTER NOT EXISTS {
        ?permission odrl:constraint ?constraint .
    }
    FILTER (?action = tosl:terminate ||
            ?action = tosl:suspend ||
            ?action = tosl:remove ||
            ?action = tosl:disble)
}