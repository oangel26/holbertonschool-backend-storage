-- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.

CREATE TRIGGER decreases_the_quantity AFTER INSERT ON orders
    FOR EACH ROW
        UPDATE items SET quantity = quantity - NEW.number
        WHERE items.name = NEW.item_name;
