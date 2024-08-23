import chromadb

# Initialize ChromaDB client
chroma_client = chromadb.Client()

# Create a collection for customer support-related documents
collection = chroma_client.create_collection(name="customer_support")

# Adding customer support-oriented documents with IDs
# By default, Chroma uses all-MiniLM-L6-v2 for embedding
collection.add(
    documents=[
        "Our products come with a 2-year warranty covering manufacturing defects and hardware failures.",
        "Customers can return products within 30 days of purchase if unsatisfied. The product must be in its original condition.",
        "Standard shipping takes 5-7 business days. Express shipping options are available at an additional cost.",
        "Technical support is available 24/7 through our helpline and chat service for troubleshooting and product queries.",
        "Software updates for products are released quarterly to enhance functionality and security.",
        "Customers can manage their accounts online to update personal details, track orders, and manage subscriptions.",
        "We accept all major credit cards, PayPal, and bank transfers. Payment through cryptocurrencies is not supported at this time.",
        "In the event of a product recall, customers will be notified via email and can visit our website for further instructions."
    ],
    ids=[
        "warranty_policy",
        "return_policy",
        "shipping_info",
        "tech_support",
        "software_updates",
        "account_management",
        "payment_methods",
        "product_recalls"
    ]
)

# Example query to find documents related to return policies
results = collection.query(
    query_texts=["What is the return policy?"],  # Chroma will embed and query this text for you
    n_results=1  # how many results to return
)
print("Query result:", results)
