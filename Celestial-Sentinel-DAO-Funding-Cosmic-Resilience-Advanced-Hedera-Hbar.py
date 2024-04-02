# Advanced Python code for interacting with Hedera HBAR and smart contracts
# Note: You'll need to install the 'hedera-sdk' package (pip install hedera-sdk)

from hedera import (
    Client,
    PrivateKey,
    AccountId,
    Hbar,
    ContractId,
    ContractFunctionParams,
    ContractFunctionResult,
    ContractCallQuery,
    ContractExecuteTransaction,
)

# Replace these with your actual account details
YOUR_PRIVATE_KEY = "your_private_key_here"
YOUR_ACCOUNT_ID = AccountId.fromString("your_account_id_here")
CONTRACT_ID = ContractId.fromString("contract_id_here")  # Replace with your contract ID

def transfer_hbar_to_contract(contract_id, amount_hbar):
    # Initialize the Hedera client
    client = Client.forTestnet()

    # Set your account ID and private key
    client.setOperator(YOUR_ACCOUNT_ID, PrivateKey.fromString(YOUR_PRIVATE_KEY))

    # Create a contract call query to get the contract's current balance
    query = ContractCallQuery(contract_id, "getBalance")
    query.setGas(100_000)  # Set gas limit

    # Execute the query
    result = query.execute(client)
    current_balance = result.getString(0)  # Assuming the contract returns balance as a string

    print(f"Current contract balance: {current_balance} HBAR")

    # Create a contract execute transaction to transfer HBAR to the contract
    transfer = ContractExecuteTransaction()
    transfer.setContractId(contract_id)
    transfer.setFunctionParams(ContractFunctionParams().addString("transfer").addInt(amount_hbar))

    # Sign and submit the transaction
    transaction_id = transfer.execute(client)
    transaction_id_str = transaction_id.toString()

    print(f"Transaction submitted! Transaction ID: {transaction_id_str}")

if __name__ == "__main__":
    # Example usage: Transfer 10 HBAR to the smart contract
    transfer_hbar_to_contract(CONTRACT_ID, 10)
