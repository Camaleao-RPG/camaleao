# Probability Analysis for an RPG Dice Pool System (D20)

This project calculates probabilities for a dice pool system used in RPGs, where the **D20** is the main die.
The system features:

- **Critical Success** (roll of 20) = +2 successes
- **Normal Success** (roll ≥ DT and < 20) = +1 success
- **Failure** (roll < DT and > 1) = 0 successes
- **Critical Failure** (roll of 1) = −1 success

It generates a **CSV table** with probabilities of achieving at least `k` successes (and exactly `k` successes), for:

- Dice pool sizes from 1 to 18
- Target Difficulties (DT) from 20 down to 3 (even and odd in separate columns)

## Output format

The CSV contains two vertical blocks:

- **Even DTs** (20, 18, …, 4) on the left
- **Odd DTs** (19, 17, …, 3) on the right

Each cell is formatted as:

```
≥k (=k)
```

where:

- `≥k` = probability of at least `k` total successes
- `(=k)` = probability of exactly `k` total successes
  Empty cells indicate probabilities that round to zero.

### CSV example

| Nº de d20 | DT  | ≥1 (=1)       | ≥2 (=2)       | ≥3 (=3)       | DT  | ≥1 (=1)       | ≥2 (=2)       | ≥3 (=3)       |
| --------- | --- | ------------- | ------------- | ------------- | --- | ------------- | ------------- | ------------- |
| 1         | 20  | 05.00 (00.00) | 05.00 (05.00) |               | 19  | 10.00 (05.00) | 05.00 (05.00) |               |
| 2         |     | 09.75 (00.50) | 09.25 (09.00) | 00.25 (00.00) |     | 18.50 (09.00) | 09.50 (08.75) | 00.75 (00.50) |
| 3         |     | 14.23 (01.35) | 12.88 (12.15) | 00.73 (00.04) |     | 25.75 (12.15) | 13.60 (11.55) | 02.50 (01.33) |

## How to run

```bash
python main.py
```

This will generate `prob_dice_pool_d20.csv` in the project folder.
