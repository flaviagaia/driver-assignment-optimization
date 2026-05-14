# driver-assignment-optimization

## Português

### Visão geral

`driver-assignment-optimization` é um projeto de atribuição de motoristas a pedidos, inspirado em uma pergunta clássica de marketplace: **como construir uma lógica de assignment entre pedido e entregador**.

O projeto simula candidatos por pedido e escolhe o melhor entregador com um score que combina:

- probabilidade de aceitação;
- distância até o pickup;
- atraso estimado no pickup;
- utilização do entregador.

### Objetivo analítico

O projeto trata assignment como um problema inicial de **ranking / scoring**, antes de uma camada mais sofisticada de optimization.

Isso é útil porque mostra o primeiro passo correto:

- definir sinais relevantes;
- construir um score auditável;
- medir o perfil médio das escolhas;
- só depois evoluir para otimização mais complexa.

### Função de score

O score atual combina:

- `driver_accept_prob` com peso positivo forte
- `utilization_score` com peso positivo moderado
- `distance_to_pickup_km` com penalidade
- `estimated_pickup_delay_min` com penalidade

### Estrutura dos dados

Cada linha representa um candidato `order-driver` com:

- `order_id`
- `driver_id`
- `region`
- `distance_to_pickup_km`
- `estimated_pickup_delay_min`
- `driver_accept_prob`
- `utilization_score`

### Técnicas e bibliotecas

- heuristic scoring
- greedy assignment
- `Python`
- `csv`
- `json`
- `pathlib`
- `unittest`

### Resultados atuais

- `candidate_row_count = 320`
- `assigned_order_count = 80`
- `avg_assignment_score = 0.2695`
- `avg_distance_to_pickup_km = 0.9645`
- `avg_estimated_pickup_delay_min = 6.4621`
- `avg_driver_accept_prob = 0.8406`

### Artefatos gerados

- [optimized_assignments.json](data/processed/optimized_assignments.json)
- [driver_assignment_report.json](data/processed/driver_assignment_report.json)

### Arquivos principais

- [main.py](main.py)
- [src/data_factory.py](src/data_factory.py)
- [src/modeling.py](src/modeling.py)
- [tests/test_project.py](tests/test_project.py)

### Como executar

```bash
python3 main.py
python3 -m unittest discover -s tests -v
python3 -m py_compile main.py src/data_factory.py src/modeling.py tests/test_project.py
```


## English

### Overview

`driver-assignment-optimization` is a driver-to-order assignment project built around a common marketplace question: **how to build an assignment logic between orders and couriers**.

The project simulates candidate matches per order and selects the best courier using a score that combines:

- acceptance probability;
- pickup distance;
- estimated pickup delay;
- courier utilization.

### Analytical objective

The project frames assignment as an initial **ranking / scoring** problem before a more advanced optimization layer.

This is useful because it shows the correct first step:

- define relevant signals;
- build an auditable score;
- measure the profile of selected matches;
- then evolve toward more complex optimization.

### Scoring function

The current score combines:

- `driver_accept_prob` with a strong positive weight
- `utilization_score` with a moderate positive weight
- `distance_to_pickup_km` as a penalty
- `estimated_pickup_delay_min` as a penalty

### Data structure

Each row represents one `order-driver` candidate with:

- `order_id`
- `driver_id`
- `region`
- `distance_to_pickup_km`
- `estimated_pickup_delay_min`
- `driver_accept_prob`
- `utilization_score`

### Techniques and libraries

- heuristic scoring
- greedy assignment
- `Python`
- `csv`
- `json`
- `pathlib`
- `unittest`

### Current results

- `candidate_row_count = 320`
- `assigned_order_count = 80`
- `avg_assignment_score = 0.2695`
- `avg_distance_to_pickup_km = 0.9645`
- `avg_estimated_pickup_delay_min = 6.4621`
- `avg_driver_accept_prob = 0.8406`

### Generated artifacts

- [optimized_assignments.json](data/processed/optimized_assignments.json)
- [driver_assignment_report.json](data/processed/driver_assignment_report.json)

### Main files

- [main.py](main.py)
- [src/data_factory.py](src/data_factory.py)
- [src/modeling.py](src/modeling.py)
- [tests/test_project.py](tests/test_project.py)

### How to run

```bash
python3 main.py
python3 -m unittest discover -s tests -v
python3 -m py_compile main.py src/data_factory.py src/modeling.py tests/test_project.py
```

