CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    doc_id VARCHAR(100) NOT NULL,
    shop_num INTEGER NOT NULL,
    cash_num INTEGER NOT NULL,
    item VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    amount INTEGER NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    discount NUMERIC(10,2) DEFAULT 0,
    total_sum NUMERIC(10,2) NOT NULL,
    source_file VARCHAR(255),
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT sales_unique UNIQUE (
            doc_id,
            shop_num,
            cash_num,
            item,
            category,
            amount,
            price,
            discount
        )
);