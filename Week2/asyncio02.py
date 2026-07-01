# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.
import asyncio
async def greet():
    print("Hello, World!")


coroutine_object = greet()


print(type(coroutine_object))  # <class 'coroutine'>

coro_object.close()  # Close the coroutine object to free up resources