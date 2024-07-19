# Reward Function CHANGELOG

## branch: pato-calcular-racin-line-optima
Calculates reward based on:
- avoiding zigzag
- optimal racing line

## branch: reward-function-1
Calculates reward based on:
- avoiding zigzag
- optimal racing line
- not having all wheels on track heavily penalizes

## branch: reward-function-2
Calculates reward based on:
- avoiding zigzag
- optimal racing line
- not having all wheels on track heavily penalizes
- the reward is now a continuous function based on the distance to the optimal racing line passed through e^-5x
