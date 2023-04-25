import asyncpg


async def get_database_connection():
    conn = await asyncpg.connect(user='JokyOFC',
                                 password='K7hPwI5liaWj',
                                 database='neondb',
                                 host='ep-summer-leaf-890766.us-east-2.aws.neon.tech')
    return conn
