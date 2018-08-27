UPDATE: Considering putting a halt on this as backend is causing some trouble and needs lots of work. Redo simpler?

Buildscript for production deployment:

cd frontend

1) Build the frontend
yarn build

2) Move files at the build root inside a root subdirectory

mkdir -p build/rootfor file in $(ls build | grep -E -v '^(index\.html|static|root)$'); do
    mv "build/$file" build/root;
done
cd ..
cd backend
pipenv shell

3) Build the backend

./manage.py collectstatic --no-input
cd ..
