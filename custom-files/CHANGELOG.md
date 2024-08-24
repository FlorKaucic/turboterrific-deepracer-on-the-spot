# turboterrific-sf-v3-oas2

- branch: optimal-action-space-test
- model base: -
- model name: turboterrific-sf-v3-oas2
- changes:
  - optimal action space with min speed 1.2
- training: 240 min
- url: http://18.232.180.79:8100/menu.html

# turboterrific-sf-v3-oas2-batch32

- branch: optimal-action-space-test
- model base: turboterrific-sf-v3-oas2
- model name: turboterrific-sf-v3-oas2-batch32
- changes:
  - batch_size: 32
- training: 240 min
- url: http://3.90.164.82:8100/menu.html
