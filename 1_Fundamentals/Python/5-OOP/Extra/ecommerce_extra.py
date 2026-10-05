# ecommerce.py
class Product:
    """
    Represents a product with a SKU, name, and price.
    """

    def __init__(
        self,
        sku: str,
        name: str,
        price: float,
    ):
        """
        Initializes a new Product instance.

        Args:
            sku (str): The Stock Keeping Unit, a unique identifier for the product.
            name (str): The name of the product.
            price (float): The price of the product.
        """
        # TODO in task 2.0

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A string showing the product's name, SKU, and price.
        """
        # TODO in task 2.0


class Shoes(Product):
    """
    Represents a shoe product, inheriting from Product, with additional attributes for size and color.
    """

    def __init__(
        self,
        sku: str,
        name: str,
        price: float,
        size: int,
        color: str,
    ):
        """
        Initializes a new Shoes instance.

        Args:
            sku (str): The Stock Keeping Unit.
            name (str): The name of the shoe.
            price (float): The price of the shoe.
            size (int): The size of the shoe.
            color (str): The color of the shoe.
        """
        super().__init__(sku, name, price)
        # TODO in task 2.0

    def __str__(self):
        """
        Returns a string representation of the shoe, including details from the parent Product class.

        Returns:
            str: A string showing shoe details, including size and color.
        """
        # TODO in task 2.0


class Electronics(Product):
    """
    Represents an electronics product, inheriting from Product, with additional attributes for brand and warranty.
    """

    def __init__(
        self,
        sku: str,
        name: str,
        price: float,
        brand: str,
        warranty_period: int,
    ):
        """
        Initializes a new Electronics instance.

        Args:
            sku (str): The Stock Keeping Unit.
            name (str): The name of the electronic device.
            price (float): The price of the device.
            brand (str): The brand of the device.
            warranty_period (int): The warranty period in months.
        """
        super().__init__(sku, name, price)
        # TODO in task 2.0

    def __str__(self):
        """
        Returns a string representation of the electronics product, including details from the parent Product class.

        Returns:
            str: A string showing electronics details, including brand and warranty.
        """
        # TODO in task 2.0


class Furniture(Product):
    """
    Represents a furniture product, inheriting from Product, with attributes for material and dimensions.
    """

    def __init__(
        self,
        sku: str,
        name: str,
        price: float,
        material: str,
        dimensions: str,
    ):
        """
        Initializes a new Furniture instance.

        Args:
            sku (str): The Stock Keeping Unit.
            name (str): The name of the furniture item.
            price (float): The price of the item.
            material (str): The material the furniture is made of.
            dimensions (str): The dimensions of the furniture (e.g., "36x24x18 inches").
        """
        super().__init__(sku, name, price)
        # TODO in task 2.0

    def __str__(self):
        """
        Returns a string representation of the furniture product, including details from the parent Product class.

        Returns:
            str: A string showing furniture details, including material and dimensions.
        """
        # TODO in task 2.0


class Warehouse:
    """
    Manages the inventory of products.
    """

    def __init__(
        self,
        company_name: str,
    ):
        """
        Initializes a new Warehouse instance.

        Args:
            company_name (str): The name of the company that owns the warehouse.
        """
        # TODO in task 1.0

    def __str__(self) -> str:
        """
        Returns a string representation of the warehouse.

        Returns:
            str: A string indicating the warehouse's company name.
        """
        # TODO in task 1.0

    def add_product(
        self,
        product: Product,
    ) -> None:
        """
        Adds a single product instance to the warehouse inventory.

        Args:
            product (Product): The product to add.

        Returns:
            None
        """
        # TODO in task 2.1

    def remove_product(
        self,
        product: Product,
    ) -> Product | None:
        """
        Removes a single, specific product instance from the warehouse inventory.

        Args:
            product (Product): The product instance to remove.  This must be the *exact*
                               object in the inventory, not just one with the same SKU.

        Returns:
            Product | None: The removed product instance if found and removed, otherwise None.
                            Prints an error message if the product is not found.
        """
        # TODO in task 5

    def calculate_total_value(self) -> float:
        """
        Calculates the total value of all products currently in the warehouse.

        Returns:
            float: The total value (sum of all product prices).
        """
        # TODO in task 3

    def get_current_inventory(self) -> None:
        """
        Prints the current inventory of the warehouse.  Displays each product's name,
        SKU, quantity, and the total value of the warehouse.

        Returns:
            None
        """
        # TODO in task 3

    def add_multiple_products(
        self,
        product: Product,
        quantity: int,
    ) -> None:
        """
        Adds multiple copies of the *same* product instance to the warehouse.

        Args:
            product (Product): The product instance to add.  All added products will
                               be this exact object (important for later removal).
            quantity (int): The number of copies to add.

        Returns:
            None. Prints an error message if the quantity is not positive.
        """
        # OPTIONAL – add a method that allows users to add a number of a given product to the ware house

    def remove_multiple_products(
        self,
        sku: str,
        quantity: int,
    ) -> int:
        """
        Removes multiple products with the given SKU from the warehouse.

        Args:
            sku (str): The SKU of the products to remove.
            quantity (int): The number of products to attempt to remove.

        Returns:
            int: The number of products actually removed.  This may be less than
                 `quantity` if there aren't enough products with the given SKU
                 in the warehouse. Prints error messages if the SKU is not found
                 or if the quantity is invalid.
        """
        # OPTIONAL – add a method that allows users to remove a number of a given product from the warehouse


class Person:
    """
    Represents a person with a name, age, and address.
    """

    def __init__(
        self,
        name: str,
        age: int,
        address: str,
    ):
        """
        Initializes a new Person instance.

        Args:
            name (str): The person's name.
            age (int): The person's age.
            address (str): The person's address.
        """
        # TODO in task 1.0

    def __str__(self):
        """
        Returns a string representation of the person.

        Returns:
            str: A string containing the person's name, age, and address.
        """
        # TODO in task 1.0

    def introduce(self):
        """
        Prints a simple introduction of the person to standard output.

        Returns:
            None
        """
        # TODO in task 1.0


class Shopper(Person):
    """
    Represents a shopper, inheriting from Person, with an additional shopping cart.
    """

    def __init__(
        self,
        name: str,
        age: int,
        address: str,
        shopping_cart: list = None,
    ):
        """
        Initializes a new Shopper instance.

        Args:
            name (str): The shopper's name.
            age (int): The shopper's age.
            address (str): The shopper's address.
            shopping_cart (list, optional): A list of Product instances representing the shopper's
                initial shopping cart. Defaults to None (an empty cart).
        """
        super().__init__(name, age, address)
        # TODO in task 4

    def add_to_cart(self, product: Product):
        """
        Adds a product to the shopper's shopping cart.

        Args:
            product (Product): The product instance to add.

        Returns:
            None. Prints a confirmation message.
        """
        # TODO in task 4

    def view_cart(self):
        """
        Prints the contents of the shopper's shopping cart.

        Returns:
            None. Prints a message if the cart is empty.
        """
        # TODO in task 4

    def checkout(
        self,
        warehouse: Warehouse,
    ):
        """
        Simulates the checkout process.  Removes items from the warehouse,
        calculates the total cost, and verifies inventory value consistency.

        Args:
            warehouse (Warehouse): The warehouse to interact with.

        Returns:
            None. Prints the total cost and a message indicating whether the
            inventory value check passed or failed.  Clears the shopping cart
            after checkout (regardless of success).
        """

        # TODO in task 5


class Seller(Person):
    """
    Represents a seller, inheriting from Person, with an employee ID.
    """

    def __init__(
        self,
        name: str,
        age: int,
        address: str,
        employee_id: str,
    ):
        """
        Initializes a new Seller instance.

        Args:
            name (str): The seller's name.
            age (int): The seller's age.
            address (str): The seller's address.
            employee_id (str): The seller's employee ID.
        """
        # TODO in task 1.0

    def __str__(self):
        """
        Returns a string representation of the seller.

        Returns:
            str: A string containing the seller's information and employee ID.
        """
        return f"{super().__str__()}, Employee ID: {self.employee_id}"

    def add_product_to_warehouse(
        self,
        warehouse: Warehouse,
        product: Product,
    ) -> None:
        """
        Adds a product to the specified warehouse.

        Args:
            warehouse (Warehouse): The warehouse to add the product to.
            product (Product): The product to add.

        Returns:
            None. Prints a confirmation message.
        """
        # TODO in task 2.1
