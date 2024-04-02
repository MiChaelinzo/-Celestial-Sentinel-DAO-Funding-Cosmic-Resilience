# Import necessary libraries
from hedera import (
    Client,
    PrivateKey,
    AccountId,
    ContractId,
    ContractFunctionParams,
    ContractExecuteTransaction,
)

# Set your Hedera account details
YOUR_PRIVATE_KEY = "your_private_key_here"
YOUR_ACCOUNT_ID = AccountId.fromString("your_account_id_here")  # Replace with your account ID
CONTRACT_ID = ContractId.fromString("contract_id_here")  # Replace with your Guardian contract ID

def protect_earth_from_cosmic_events():
    # Initialize the Hedera client
    client = Client.forTestnet()  # Use mainnet for production

    # Set your account as the operator
    client.setOperator(YOUR_ACCOUNT_ID, PrivateKey.fromString(YOUR_PRIVATE_KEY))

    # Create a contract execute transaction to interact with the Guardian
    transaction = ContractExecuteTransaction()
    transaction.setContractId(CONTRACT_ID)
    transaction.setFunctionParams(ContractFunctionParams().addString("protectEarth"))

    # Sign and submit the transaction
    transaction_id = transaction.execute(client)
    transaction_id_str = transaction_id.toString()

    print(f"Transaction submitted! Transaction ID: {transaction_id_str}")

if __name__ == "__main__":
    protect_earth_from_cosmic_events()
