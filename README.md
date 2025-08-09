# Probability Analysis for an RPG Dice Pool System (D20)

This project calculates probabilities for a dice pool system used in RPGs, where the **D20** is the main die.
The system features:

* **Critical Success** (roll of 20) = +2 successes
* **Normal Success** (roll ≥ DT and < 20) = +1 success
* **Failure** (roll < DT and > 1) = 0 successes
* **Critical Failure** (roll of 1) = −1 success

It generates a **CSV table** with probabilities of achieving at least `k` successes (and exactly `k` successes), for:

* Dice pool sizes from 1 to 18
* Target Difficulties (DT) from 20 down to 3 (even and odd in separate columns)

## Output format

The CSV contains two vertical blocks:

* **Even DTs** (20, 18, …, 4) on the left
* **Odd DTs** (19, 17, …, 3) on the right

Each cell is formatted as:

```
≥k% (=k%)
```

where:

* `≥k%` = probability of at least `k` total successes
* `(=k%)` = probability of exactly `k` total successes
  Empty cells indicate probabilities that round to zero.

### CSV example

```
, , Número de sucessos, , , , , , , , , Número de sucessos, , , , , , , , , ,
Número de d20, DT do dado, ≥1 (=1), ≥2 (=2), ≥3 (=3), ≥4 (=4), ≥5 (=5), ≥6 (=6), ≥7 (=7), ≥8 (=8), ≥9 (=9), ≥10 (=10), DT do dado, ≥1 (=1), ≥2 (=2), ≥3 (=3), ≥4 (=4), ≥5 (=5), ≥6 (=6), ≥7 (=7), ≥8 (=8), ≥9 (=9), ≥10 (=10)
1, 20, 05.00% (00.00%), 05.00% (05.00%), , , , , , , , , 19, 10.00% (05.00%), 05.00% (05.00%), , , , , , , , ,
2,    , 09.75% (03.50%), 07.00% (02.50%), 03.00% (01.00%), , , , , , , ,     , 15.00% (05.25%), 08.50% (03.00%), 04.25% (01.75%), , , , , , , ,
3,    , 14.25% (05.00%), 10.50% (03.75%), 06.00% (02.25%), 02.50% (01.00%), , , , , , ,     , 20.50% (07.00%), 12.00% (04.25%), 06.50% (02.50%), 03.00% (01.25%), , , , , , ,
```

## How to run

```bash
python main.py
```

This will generate `prob_dice_pool_d20.csv` in the project folder.
