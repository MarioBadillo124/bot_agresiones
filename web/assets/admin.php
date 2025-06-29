<?php
require_once 'db/conexion.php';


// Función para obtener usuarios
function obtenerUsuarios($conn, $filtros = []) {
    $where = [];
    $params = [];
    $types = '';

    if (!empty($filtros['search'])) {
        $where[] = "(usuario LIKE ? OR correo LIKE ?)";
        $searchTerm = '%' . $filtros['search'] . '%';
        $params[] = $searchTerm;
        $params[] = $searchTerm;
        $types .= 'ss';
    }

    if (!empty($filtros['role'])) {
        $where[] = "rol = ?";
        $params[] = $filtros['role'];
        $types .= 's';
    }

    if (!empty($filtros['status'])) {
        $where[] = "estado = ?";
        $params[] = $filtros['status'];
        $types .= 's';
    }

    $query = "SELECT * FROM usuarios";
    if (!empty($where)) {
        $query .= " WHERE " . implode(" AND ", $where);
    }

    $stmt = $conn->prepare($query);
    if (!empty($params)) {
        $stmt->bind_param($types, ...$params);
    }
    $stmt->execute();
    return $stmt->get_result();
}

// Procesar búsqueda/filtros
$filtros = [
    'search' => $_GET['search'] ?? '',
    'role' => $_GET['role'] ?? '',
    'status' => $_GET['status'] ?? ''
];

// Obtener usuarios
$result = obtenerUsuarios($conn, $filtros);
$usuarios = [];
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $usuarios[] = $row;
    }
}

// Mostrar mensajes
$success = $_GET['success'] ?? '';
$errors = isset($_GET['errors']) ? explode(',', $_GET['errors']) : [];
?>

<!DOCTYPE html>
<html lang="es">
<!-- Resto de tu HTML -->
</html>

<?php
// Cerrar conexión
$conn->close();
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gestión de Usuarios</title>
    <link rel="stylesheet" href="css/estilos_barra_menu.css">
    <link rel="stylesheet" href="css/usuarios.css">
</head>
<body>

    <header>
        <div class="superior">
            <div class="logo">
                <img src="images/iconos/logo.jpg" alt="logo">
            </div>
            <div class="search">
                <br><h1>Vista en tiempo real</h1><br>
            </div>
        </div>

        <div class="container__menu">
            <nav>
                <ul>
                    <li><a href="menu.html"></a></li>
                    <li><a href="live-view.html">Vista en tiempo real</a></li>
                    <li><a href="incidents.html">Historico de incidentes</a></li>
                    <li><a href="statistics.html">Estadisticas</a></li>
                    <li><a href="" id="selected">Administracion</a></li>
                </ul>
            </nav>
        </div>
    </header><br>

    <div class="container">
        <div class="header">
            <h1>Sistema de Gestión de Usuarios</h1>
        </div>
        
        <!-- Formulario de Registro -->
        <div class="card">
            <h2 class="card-title">Agregar Nuevo Usuario</h2>
            <form id="userForm" action="db/guardar_usuario.php" method="POST">
                <div class="form-row">
                    <div class="form-col">
                        <div class="form-group">
                            <label for="username">Nombre de Usuario:</label>
                            <input type="text" id="username" name="username" required>
                        </div>
                    </div>
                    
                    <div class="form-col">
                        <div class="form-group">
                            <label for="email">Correo Electrónico:</label>
                            <input type="email" id="email" name="email" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="role">Rol:</label>
                            <select id="role" name="role" required>
                                <option value="">Seleccionar Rol</option>
                                <option value="administrador">Administrador</option>
                                <option value="director">Director</option>
                                <option value="profesor">Profesor</option>
                            </select>
                        </div>
                    </div>
                    
                    <div class="form-col">
                        <div class="form-group">
                            <label for="password">Contraseña:</label>
                            <input type="password" id="password" name="password" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="confirm_password">Confirmar Contraseña:</label>
                            <input type="password" id="confirm_password" name="confirm_password" required>
                        </div>
                    </div>
                    
                    <div class="form-col">
                        <div class="form-group">
                            <label for="status">Estado:</label>
                            <select id="status" name="status" required>
                                <option value="activo">Activo</option>
                                <option value="inactivo">Inactivo</option>
                            </select>
                        </div>
                    </div>
                </div>
                
                <div class="button-group">
                    <button type="reset" class="btn btn-cancel">Cancelar</button>
                    <button type="submit" class="btn btn-save">Guardar Usuario</button>
                </div>
            </form>
        </div>
        
        <!-- Sección de Búsqueda -->
        <div class="card">
            <h2 class="card-title">Buscar Usuarios</h2>
            <div class="search-section">
                <form method="GET" action="">
                    <div class="search-input">
                        <input type="text" id="searchInput" name="search" placeholder="Buscar por usuario o email..." value="<?php echo isset($_GET['search']) ? htmlspecialchars($_GET['search']) : ''; ?>">
                    </div>
                    <div class="search-filter">
                        <select id="roleFilter" name="role">
                            <option value="">Todos los roles</option>
                            <option value="administrador" <?php echo (isset($_GET['role']) && $_GET['role'] == 'administrador') ? 'selected' : ''; ?>>Administrador</option>
                            <option value="director" <?php echo (isset($_GET['role']) && $_GET['role'] == 'director') ? 'selected' : ''; ?>>Director</option>
                            <option value="profesor" <?php echo (isset($_GET['role']) && $_GET['role'] == 'profesor') ? 'selected' : ''; ?>>Profesor</option>
                        </select>
                    </div>
                    <div class="search-filter">
                        <select id="statusFilter" name="status">
                            <option value="">Todos los estados</option>
                            <option value="activo" <?php echo (isset($_GET['status']) && $_GET['status'] == 'activo') ? 'selected' : ''; ?>>Activo</option>
                            <option value="inactivo" <?php echo (isset($_GET['status']) && $_GET['status'] == 'inactivo') ? 'selected' : ''; ?>>Inactivo</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-search">Buscar</button>
                </form>
            </div>
            
            <!-- Tabla de Usuarios Registrados -->
            <table id="usersTable">
                <thead>
                    <tr>
                        <th>Usuario</th>
                        <th>Email</th>
                        <th>Rol</th>
                        <th>Estado</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($usuarios as $usuario): ?>
                        <tr>
                            <td><?php echo htmlspecialchars($usuario['usuario'] ?? ''); ?></td>
                            <td><?php echo htmlspecialchars($usuario['correo'] ?? ''); ?></td>
                            <td><?php echo htmlspecialchars($usuario['rol'] ?? ''); ?></td>
                            <td class="status-<?php echo ($usuario['estado'] ?? '') == 'activo' ? 'active' : 'inactive'; ?>">
                                <?php echo htmlspecialchars($usuario['estado'] ?? ''); ?>
                            </td>
                            <td class="actions">
                                <button class="btn btn-action btn-edit" data-id="<?php echo $usuario['id']; ?>">Editar</button>
                                <button class="btn btn-action btn-delete" data-id="<?php echo $usuario['id']; ?>">Eliminar</button>
                            </td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        </div>
    </div>

    <script src="js/admin.js"></script>
</body>
</html>