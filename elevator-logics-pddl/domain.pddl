(define (domain elevator)
  (:requirements :strips :typing :equality :numeric-fluents)
  (:types floor person - object)
  
  (:predicates
    (elevator-at ?f - floor)
    (person-at ?p - person ?f - floor)
    (person-in ?p - person)
  )
  
  (:functions
    (passenger-count) ; Função para contar o número de passageiros no elevador
  )
  
  (:action move-up
    :parameters (?from - floor ?to - floor)
    :precondition (and (elevator-at ?from) (<= (passenger-count) 5))
    :effect (and (elevator-at ?to) (not (elevator-at ?from)))
  )
  
  (:action move-down
    :parameters (?from - floor ?to - floor)
    :precondition (and (elevator-at ?from) (<= (passenger-count) 5))
    :effect (and (elevator-at ?to) (not (elevator-at ?from)))
  )
  
  (:action enter
    :parameters (?p - person ?f - floor)
    :precondition (and (person-at ?p ?f) (elevator-at ?f) (< (passenger-count) 5))
    :effect (and (person-in ?p) (not (person-at ?p ?f)) (increase (passenger-count) 1))
  )
  
  (:action exit
    :parameters (?p - person ?f - floor)
    :precondition (and (person-in ?p) (elevator-at ?f))
    :effect (and (person-at ?p ?f) (decrease (passenger-count) 1))
  )
)
