# Example Python code for interacting with Hedera HBAR
# Note: You'll need to install the 'hedera-sdk' package (pip install hedera-sdk)

from hedera import (
    Client,
    PrivateKey,
    AccountId,
    Hbar,
    TransactionId,
    TransferTransaction,
)

# Replace these with your actual account details
YOUR_PRIVATE_KEY = "your_private_key_here"
YOUR_ACCOUNT_ID = AccountId.fromString("your_account_id_here")

def transfer_hbar(recipient_account_id, amount_hbar):
    # Initialize the Hedera client
    client = Client.forTestnet()

    # Set your account ID and private key
    client.setOperator(YOUR_ACCOUNT_ID, PrivateKey.fromString(YOUR_PRIVATE_KEY))

    # Create a transfer transaction
    transfer = TransferTransaction()
    transfer.setTransactionMemo("Supporting Celestial Sentinel DAO")
    transfer.setMaxTransactionFee(Hbar(1))  # Set your desired fee

    # Add the recipient account and amount
    transfer.addHbarTransfer(recipient_account_id, Hbar(amount_hbar))

    # Sign and submit the transaction
    transaction_id = transfer.execute(client)
    transaction_id_str = transaction_id.toString()

    print(f"Transaction submitted! Transaction ID: {transaction_id_str}")

if __name__ == "__main__":
    # Example usage: Transfer 10 HBAR to a recipient account
    recipient_account = AccountId.fromString("recipient_account_id_here")
    transfer_hbar(recipient_account, 10)
