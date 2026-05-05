# driver-assignment-optimization

## Português

`driver-assignment-optimization` é um projeto inspirado em uma pergunta típica de DoorDash: **como construir uma lógica de atribuição de motoristas a pedidos**.

O projeto simula candidatos de matching por pedido e escolhe o melhor entregador usando um score que combina:

- probabilidade de aceitação;
- distância até o pickup;
- atraso estimado no pickup;
- utilização do entregador.

## Objetivo analítico

O projeto trata driver assignment como um problema inicial de **ranking / scoring**, não ainda como uma camada completa de optimization.

Isso é útil em entrevista porque mostra o primeiro passo correto:

- definir os sinais relevantes;
- construir um score auditável;
- medir o perfil médio das escolhas;
- só depois evoluir para matching mais sofisticado.

## O que o projeto faz

1. gera candidatos sintéticos de order-driver matching;
2. calcula um score por candidato;
3. escolhe o melhor candidato por pedido;
4. resume a qualidade da política de atribuição.

## Função de score

O score atual combina:

- `driver_accept_prob` com peso positivo forte
- `utilization_score` com peso positivo moderado
- `distance_to_pickup_km` com penalidade
- `estimated_pickup_delay_min` com penalidade

Esse desenho tenta equilibrar aceitação, eficiência e tempo operacional.

## Objetivo da otimização

- maximizar aceitação;
- controlar atraso de pickup;
- evitar distância excessiva;
- manter utilização saudável.

## Técnicas e bibliotecas

- heuristic scoring
- greedy assignment
- `Python`
- `csv`
- `json`
- `pathlib`
- `unittest`

## Contrato dos dados

Cada linha representa um candidato `order-driver` com:

- `order_id`
- `driver_id`
- `region`
- `distance_to_pickup_km`
- `estimated_pickup_delay_min`
- `driver_accept_prob`
- `utilization_score`

## Resultados atuais

- `candidate_row_count = 320`
- `assigned_order_count = 80`
- `avg_assignment_score = 0.2695`
- `avg_distance_to_pickup_km = 0.9645`
- `avg_estimated_pickup_delay_min = 6.4621`
- `avg_driver_accept_prob = 0.8406`

## Artefatos gerados

- [optimized_assignments.json](/Users/flaviagaia/Documents/CV_FLAVIA_CODEX/driver-assignment-optimization/data/processed/optimized_assignments.json)
- [driver_assignment_report.json](/Users/flaviagaia/Documents/CV_FLAVIA_CODEX/driver-assignment-optimization/data/processed/driver_assignment_report.json)

## Como executar

```bash
python3 main.py
python3 -m unittest discover -s tests -v
python3 -m py_compile main.py src/data_factory.py src/modeling.py tests/test_project.py
```

## Como defender em entrevista

> Para driver assignment, eu começaria com uma política de ranking simples e auditável, combinando aceitação esperada, distância ao pickup, delay estimado e utilização. Esse projeto mostra exatamente esse primeiro passo antes de evoluir para um matching ou optimization layer mais sofisticado.
