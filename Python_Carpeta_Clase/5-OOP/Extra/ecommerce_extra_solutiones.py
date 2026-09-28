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
        self.sku = sku
        self.name = name
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A string showing the product's name, SKU, and price.
        """
        return f"{self.name}\n  - SKU: {self.sku}\n  - Price: {self.price}"


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
        self.size = size
        self.color = color

    def __str__(self):
        """
        Returns a string representation of the shoe, including details from the parent Product class.

        Returns:
            str: A string showing shoe details, including size and color.
        """
        return f"{super().__str__()}\n  - Size: {self.size}\n  - Color: {self.color}"


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
        self.brand = brand
        self.warranty_period = warranty_period

    def __str__(self):
        """
        Returns a string representation of the electronics product, including details from the parent Product class.

        Returns:
            str: A string showing electronics details, including brand and warranty.
        """
        return f"{super().__str__()}\n  - Brand: {self.brand}\n  - Warranty: {self.warranty_period} months"


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
        self.material = material
        self.dimensions = dimensions

    def __str__(self):
        """
        Returns a string representation of the furniture product, including details from the parent Product class.

        Returns:
            str: A string showing furniture details, including material and dimensions.
        """
        return f"{super().__str__()}\n  - Material: {self.material}\n  - Dimensions: {self.dimensions}"


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
        self.company_name = company_name
        self.__current_inventory = {}  # Private attribute to store inventory

    def __str__(self) -> str:
        """
        Returns a string representation of the warehouse.

        Returns:
            str: A string indicating the warehouse's company name.
        """
        return f"Warehouse of {self.company_name} ltd"

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
        if product.sku not in self.__current_inventory:
            self.__current_inventory[product.sku] = []

        self.__current_inventory[product.sku].append(product)

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
        if (
            product.sku in self.__current_inventory
            and self.__current_inventory[product.sku]
        ):
            return self.__current_inventory[product.sku].pop()
        else:
            print(f"Product {product.sku} not found in warehouse")
            return None

    def calculate_total_value(self) -> float:
        """
        Calculates the total value of all products currently in the warehouse.

        Returns:
            float: The total value (sum of all product prices).
        """
        total_value = 0
        for products in self.__current_inventory.values():
            for product in products:
                total_value += product.price
        return total_value

    def get_current_inventory(self) -> None:
        """
        Prints the current inventory of the warehouse.  Displays each product's name,
        SKU, quantity, and the total value of the warehouse.

        Returns:
            None
        """

        print(f"Current inventory in {self}:")
        for sku, products in self.__current_inventory.items():
            if products is None or len(products) == 0:
                print(f"- SKU: {sku}: 0 units")
                continue

            print(f"- {products[0].name} (SKU: {sku}): {len(products)} units")

        print(f"Total value of warehouse: {self.calculate_total_value()}")

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
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        if product.sku not in self.__current_inventory:
            self.__current_inventory[product.sku] = []
        self.__current_inventory[product.sku].extend([product] * quantity)

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
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return 0

        if sku not in self.__current_inventory:
            print(f"Product with SKU {sku} not found in warehouse.")
            return 0

        available_quantity = len(self.__current_inventory[sku])
        if available_quantity == 0:
            print(f"No units of product with SKU {sku} in warehouse.")
            return 0

        products_to_remove = min(quantity, available_quantity)
        products = self.__current_inventory[sku]
        for _ in range(products_to_remove):
            products.pop()

        return products_to_remove


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
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        """
        Returns a string representation of the person.

        Returns:
            str: A string containing the person's name, age, and address.
        """
        return f"Name: {self.name}\n - Age: {self.age}\n - Address: {self.address}"

    def introduce(self):
        """
        Prints a simple introduction of the person to standard output.

        Returns:
            None
        """
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


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
        self.shopping_cart = shopping_cart if shopping_cart else []

    def add_to_cart(self, product: Product):
        """
        Adds a product to the shopper's shopping cart.

        Args:
            product (Product): The product instance to add.

        Returns:
            None. Prints a confirmation message.
        """
        self.shopping_cart.append(product)
        print(f"{product.name} added to cart.")

    def view_cart(self):
        """
        Prints the contents of the shopper's shopping cart.

        Returns:
            None. Prints a message if the cart is empty.
        """
        if not self.shopping_cart:
            print("Your cart is empty.")
            return
        print("Your cart contains:")
        for product in self.shopping_cart:
            print(f"- {product}")

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

        initial_warehouse_value = warehouse.calculate_total_value()
        expected_value_reduction = sum(product.price for product in self.shopping_cart)

        total_cost = 0
        for product in self.shopping_cart:
            removed_product = warehouse.remove_product(
                product
            )  # Remove the *exact* product instance
            if removed_product:
                total_cost += removed_product.price
            else:
                print(f"Product {product.sku} is out of stock.")

        print(f"Total cost: {total_cost}")

        expected_post_checkout_value = (
            initial_warehouse_value - expected_value_reduction
        )
        actual_post_checkout_value = warehouse.calculate_total_value()

        if (
            abs(expected_post_checkout_value - actual_post_checkout_value) < 1e-6
        ):  # Using a tolerance for float comparison
            print("Inventory value check passed.")
        else:
            print("WARNING: Inventory value mismatch!")
            print(f"  Expected value after checkout: {expected_post_checkout_value}")
            print(f"  Actual value after checkout:   {actual_post_checkout_value}")
        self.shopping_cart = []  # Empty the cart after checkout


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
        super().__init__(name, age, address)
        self.employee_id = employee_id

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
        warehouse.add_product(product)
        print(f"Product {product.name} added to the warehouse.")
