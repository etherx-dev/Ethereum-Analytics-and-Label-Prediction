INSERT `ethereum-262008.mergedDataset.mining` (from_address, nonce, to_address, gas, gas_price, value, block_number, block_timestamp)
(SELECT from_address, nonce, to_address, gas, gas_price, value, block_number, block_timestamp
FROM `ethereum-262008.ethupdated.mining` WHERE 1=1)

INSERT `ethereum-262008.mergedDataset.mining` (from_address, nonce, to_address, gas, gas_price, value, block_number, block_timestamp)
(SELECT from_address, nonce, to_address, gas, gas_price, value, block_number, block_timestamp
FROM `ethereum-262008.ethupdated.mining2` WHERE 1=1)
