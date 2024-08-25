import duckdb  

def create_db():
    result = duckdb.sql("""
        SELECT
        station,
        min(temperatura) as min_temp,
        avg(temperatura) as med_temp,
        max(temperatura) as max_temp 
        FROM read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep = ';', columns={'station':VARCHAR, 'temperatura': 'DECIMAL(3,1)'})
        GROUP BY station
    """)
    
    result.show()

if  __name__ == "__main__":
    import time 
    start_time = time.time()
    create_db()
    took = time.time()-start_time 
    print(f'Levou: {took:.2f} segundos')
    