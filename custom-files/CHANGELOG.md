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
- the reward is now a continuous function based on the distance to the optimal racing line passed through 1-x

#### Notes:
- the reward is now using 1-x, but we attempted to use e^-5x, although evaluation lap took over 1min to complete for that model
- also attempted to revert the changes in the action space (added intermediate options for turning) but this also proved to be worse

## branch: fast-and-furious
Calculates rewards based on the changes in reward-function-2.\
Modified action space to have higher speed values (but had to reduce it a bit again because it was causing more chaos at the initial training)

|Best model so far on this branch|turboterrific-v8-fk-nafaf-4cont (avg lap time: 23.465)|
|---|-----------------------------------------------------------------------------------------------------------------------------|
|Currently training|continuing turboterrific-v8-fk-nafaf-4cont as turboterrific-v8-fk-nafaf-5cont-llr with a lower learning rate for fine tuning |

## branch: tokyo-drift
Based on fast-and-furious (duh, of course...)\
Increasing speed again for further training. Last testing wasn't conclusive enough.
