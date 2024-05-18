(define (problem elevator-problem) (:domain elevator)
  (:objects
  ; Lista de andares
  f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12 f13 f14 f15 f16 f17 f18 f19 f20 f21 f22 f23 f24 f25 f26 f27 f28 f29 f30 f31 f32 f33 f34 f35 f36 f37 f38 f39 f40 f41 f42 f43 f44 f45 f46 f47 f48 f49 f50 - floor
  ; Lista de pessoas
  p1 p2 p3 p4 p5 p6 p7 p8 p9 p10 p11 p12 p13 p14 p15 p16 p17 p18 p19 p20 p21 p22 p23 p24 p25 p26 p27 p28 p29 p30 p31 p32 p33 p34 p35 p36 p37 p38 p39 p40 p41 p42 p43 p44 p45 p46 p47 p48 p49 p50 - person
  )

  (:init
    (elevator-at f1)
    (= (passenger-count) 0)
    ; Inicialize a localização dos passageiros aleatoriamente
    (person-at p1 f3)
    (person-at p2 f6)
    (person-at p3 f9)
    (person-at p4 f12)
    (person-at p5 f15)
    (person-at p6 f18)
    (person-at p7 f21)
    (person-at p8 f24)
    (person-at p9 f27)
    (person-at p10 f30)
    (person-at p11 f33)
    (person-at p12 f36)
    (person-at p13 f39)
    (person-at p14 f42)
    (person-at p15 f45)
    (person-at p16 f48)
    (person-at p17 f2)
    (person-at p18 f5)
    (person-at p19 f8)
    (person-at p20 f11)
    (person-at p21 f4)
    (person-at p22 f7)
    (person-at p23 f10)
    (person-at p24 f13)
    (person-at p25 f16)
    (person-at p26 f19)
    (person-at p27 f22)
    (person-at p28 f25)
    (person-at p29 f28)
    (person-at p30 f31)
    (person-at p31 f34)
    (person-at p32 f37)
    (person-at p33 f40)
    (person-at p34 f43)
    (person-at p35 f46)
    (person-at p36 f49)
    (person-at p37 f1)
    (person-at p38 f14)
    (person-at p39 f17)
    (person-at p40 f20)
    (person-at p41 f23)
    (person-at p42 f26)
    (person-at p43 f29)
    (person-at p44 f32)
    (person-at p45 f35)
    (person-at p46 f38)
    (person-at p47 f41)
    (person-at p48 f44)
    (person-at p49 f47)
    (person-at p50 f50)
  )

  (:goal
    (and
      ; Defina os objetivos para cada passageiro aleatoriamente
      (person-at p1 f25)
      (person-at p2 f20)
      (person-at p3 f35)
      (person-at p4 f40)
      (person-at p5 f45)
      (person-at p6 f50)
      (person-at p7 f2)
      (person-at p8 f5)
      (person-at p9 f8)
      (person-at p10 f11)
      (person-at p11 f14)
      (person-at p12 f17)
      (person-at p13 f22)
      (person-at p14 f26)
      (person-at p15 f29)
      (person-at p16 f32)
      (person-at p17 f37)
      (person-at p18 f41)
      (person-at p19 f44)
      (person-at p20 f47)
      (person-at p21 f27)
      (person-at p22 f30)
      (person-at p23 f33)
      (person-at p24 f36)
      (person-at p25 f39)
      (person-at p26 f42)
      (person-at p27 f45)
      (person-at p28 f48)
      (person-at p29 f1)
      (person-at p30 f3)
      (person-at p31 f6)
      (person-at p32 f9)
      (person-at p33 f12)
      (person-at p34 f15)
      (person-at p35 f18)
      (person-at p36 f21)
      (person-at p37 f24)
      (person-at p38 f28)
      (person-at p39 f31)
      (person-at p40 f34)
      (person-at p41 f38)
      (person-at p42 f2)
      (person-at p43 f4)
      (person-at p44 f7)
      (person-at p45 f10)
      (person-at p46 f13)
      (person-at p47 f16)
      (person-at p48 f19)
      (person-at p49 f23)
      (person-at p50 f26)
    )
  )
)